
from docutils import languages, nodes, utils
from docutils.parsers.rst import Directive, directives, roles
from docutils.transforms import Transform
from docutils.utils import unescape
import docutils

from nikola.plugin_categories import RestExtension
from nikola.plugins.compile.rest import add_node
from nikola.utils import get_logger

logger = get_logger("sphinxdesign")

import datetime
import re
import types
import sys
import collections
import logging
logging.VERBOSE=15


#
# mock types which provide same interface as Sphinx so that sphinx-design can be used without Sphinx
#

class sphinx_application_Sphinx(object):
    def add_role(self,name,role):
        roles.register_local_role(name,role)
    def add_directive(self,name,cls,override=None):
        directives.register_directive(name,cls)
    def connect(self,sig,func): pass
    def add_node(self,obj,html,latex=None,text=None,man=None,texinfo=None,override=None):
        add_node(obj,html[0],html[1]) # object,visit,depart
    def add_transform(self,trsf): pass
    def add_post_transform(self,trsf): pass
    def add_config_value(self,name,default,scope): pass

class sphinx_environment_BuildEnvironment(object):
    def __init__(self):
        self.sphinx_design_css_changed=False

Env=collections.namedtuple('BuildEnvironment_fake',['docname'])
env=Env(docname='__fake__')
app=sphinx_application_Sphinx()

class sphinx_util_docutils_SphinxDirective(Directive):
    def set_source_info(self,node): pass
    @property
    def env(self): return env

class sphinx_util_docutils_SphinxRole(object):
    def __call__(self, name, rawtext, text, lineno, inliner, options={}, content=[]):
        self.rawtext,self.text,self.lineno,self.inliner,self.options,self.content=rawtext,unescape(text),lineno,inliner,options,content
        return self.run()
    def set_source_info(self,node): pass
    @property
    def env(self): return env

class sphinx_util_docutils_ReferenceRole(sphinx_util_docutils_SphinxRole):
    explicit_title_re=re.compile(r'^(.+?)\s*(?<!\x00)<(.*?)>$', re.DOTALL)
    def __call__(self, name, rawtext, text, lineno, inliner, options={}, content=[]):
        self.disabled=text.startswith('!')
        if matched:=self.explicit_title_re.match(text): self.has_explicit_title,self.title,self.target=True,unescape(matched.group(1)),unescape(matched.group(2))
        else: self.has_explicit_title,self.title,self.target=False,unescape(text),unescape(text)
        return super().__call__(name, rawtext, text, lineno, inliner, options, content)

class LoggerALaSphinx(logging.LoggerAdapter):
    def log(self,level,msg,*args,**kwargs):
        super().log(level if isinstance(level,int) else getattr(logging,level),msg,*args,**kwargs)
    def verbose(self,msg,*args,**kwargs):
        self.log(logging.VERBOSE,msg,*args,**kwargs)
    def process(self,msg,kwargs):
        extra=kwargs.setdefault('extra',{})
        for keyword in ['type','subtype','location','nonl','color','once']:
            if keyword in kwargs: extra[keyword]=kwargs.pop(keyword)
        return msg,kwargs
    def handle(self,record): self.logger.handle(record)

def sphinx_logging_getLogger(name): return LoggerALaSphinx(logging.getLogger(name),{})


def make_sphinx_stubs():
    'Inject stubs into stub sphinx.* modules'
    for m in 'sphinx sphinx.application sphinx.environment sphinx.transforms sphinx.transforms.post_transforms sphinx.util sphinx.util.logging sphinx.util.docutils sphinx.addnodes'.split():
        mm=m.split('.')
        sys.modules[m]=types.ModuleType(mm[-1],doc='Fake Sphinx (Nikola-Sphinx compatibility layer)')
        if len(mm)>1: setattr(sys.modules['.'.join(mm[:-1])],mm[-1],sys.modules[m])

    import sphinx, sphinx.application, sphinx.util, sphinx.util.docutils, sphinx.transforms, sphinx.transforms.post_transforms, sphinx.addnodes, sphinx.util.logging

    sphinx.application.Sphinx=sphinx_application_Sphinx
    sphinx.util.docutils.SphinxDirective=sphinx_util_docutils_SphinxDirective
    sphinx.util.docutils.SphinxRole=sphinx_util_docutils_SphinxRole
    sphinx.util.docutils.ReferenceRole=sphinx_util_docutils_ReferenceRole
    sphinx.transforms.SphinxTransform=Transform
    sphinx.transforms.post_transforms.SphinxPostTransform=Transform # no-op
    sphinx.environment.BuildEnvironment=sphinx_environment_BuildEnvironment
    sphinx.util.logging.getLogger=sphinx_logging_getLogger

    # pendinx_xref really, but __class__.__name__ is used for finding visitors in the writer
    class acronym(docutils.nodes.Inline,docutils.nodes.Element): pass
    sphinx.addnodes.pending_xref=acronym


make_sphinx_stubs()

class Plugin(RestExtension):
    name='sphinxdesign'
    def set_site(self,site):
        self.site=site
        # import sphinx_design
        import sys
        sys.path.append('/home/eudoxos/build/sphinx-design')
        import sphinx_design.extension
        sphinx_design.extension.setup_extension(app)
        return super(Plugin, self).set_site(site)

