# Treeview child element no collider / buggy?

## Question

**Pas** asked on 23 Jul 2020

I've got a problem with the treeview. The child element in is not fully visible in that container (see attached picture). My problem is that the child element is wider than the parent element. In my css file there is an overflow-x property and the child element does not detect it as an element. The scrollbar seems to be attached to the parent element and not to the child elements.

## Answer

**Marin Bratanov** answered on 23 Jul 2020

Hi Pascal, I can suggest you take a look at this blog post on reviewing what happens with the DOM and what CSS rules get applied where, so you can tweak the selectors and get the desired behavior. Regards, Marin Bratanov
