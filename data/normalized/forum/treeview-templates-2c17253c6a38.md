# Treeview Templates

## Question

**Nik** asked on 02 Oct 2019

Greetings! I'm trying to replicate your docs' sidenav with a Treeview component. I was trying to overwrite the category template via Treeview Templates, but i can only overwrite the item container, not the complete node. My idea was to overwrite the root category node to alter the expand icon, ... your sidenav opens child nodes with a click on the root node. Does anybody has an idea? ... Niklas

## Answer

**Marin Bratanov** answered on 02 Oct 2019

Hi Niklas, The template of the nodes is for their content so we can provide animations and expand/collapse arrows. You can have nodes expand and collapse on clicks by hooking your own click handler on the content (inside your template) and toggling the value of the Expanded field of the model. If you have older versions of our demos from about a month back, you can find a similar approach used there. I'm attaching here the two relevant components that show how we had that done - the template is its own component which bubbles up an event coming from an @onclick attached to a span in the content. The event handler toggles the Expanded field value of the model. Regards, Marin Bratanov
