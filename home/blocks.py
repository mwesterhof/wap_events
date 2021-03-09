from wagtail.core import blocks


class BarBlock(blocks.StructBlock):
    name = blocks.CharBlock()

    class Meta:
        template = 'home/blocks/bar.html'


class FooBlock(blocks.StructBlock):
    name = blocks.CharBlock()
    bars = blocks.ListBlock(BarBlock())

    class Meta:
        template = 'home/blocks/foo.html'
