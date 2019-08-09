from mistletoe import block_token, html_renderer

import staticgen.utils as utils # Gleech

class RenaissanceHTMLRenderer(html_renderer.HTMLRenderer):
    @staticmethod
    def heading_to_anchor(heading: block_token.Heading) -> str:
        #text = utils.flatten_to_text(heading)
        text = utils.get_content(heading)
        return utils.remove_nonword_chars(text)

    def render_heading(self, token):
        template = '<h{level} id="{anchor}"><a class="header-link" href="#{anchor}">{inner}</a></h{level}>'
        inner = self.render_inner(token)
        return template.format(level=token.level, anchor=self.heading_to_anchor(token), inner=inner)

    def render_block_code(self, token):
        if isinstance(token, block_token.CodeFence) and token.language in ['devnotes', 'aside']:
            template = '<aside class="{klass}">{inner}</aside>'
            inner = self.render_inner(token)
            return template.format(klass=token.language, inner=inner)
        else:
            super(RenaissanceHTMLRenderer, self).render_block_code(token)

    # # Gleech
    # def render_document(self, *args, **kwargs):
    #     # I swear to god
    #     # so super() isn't happy because this is somehow not a class method.
    #     # there are demons in this code.
    #     try:
    #         super(RenaissanceHTMLRenderer, self).render_document(*args, **kwargs)
    #     except:
    #         sys.stdout.write("args:\n")
    #         for arg in args:
    #             sys.stdout.write(str(arg) + "\n")
    #         sys.stdout.write("kwargs\n")
    #         for kwarg in kwargs:
    #             sys.stdout.write(str(kwarg) + "\n")
    #         raise
    # # it doesn't look like anything interesting is happening here.

    # def render(self, *args, **kwargs):
    #     try:
    #         #sys.stdout.write(f"start> {str(args)}\n")
    #         return super(RenaissanceHTMLRenderer, self).render(*args, **kwargs)
    #     except Exception as e:
    #         sys.stderr.write(str(e) + "\n")
    #         for arg in args:
    #             sys.stdout.write(f"err> {arg}\n")
    #         raise
