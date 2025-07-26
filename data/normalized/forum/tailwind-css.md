# Tailwind CSS

## Question

**Har** asked on 08 Jun 2021

We are using another product called Tailwind to add css classes in to our project to design the look of certain things. This however seems to have a conflict with the telerik components most specifically the combobox where when you click on it to show the items it flashes and doesn't stay open so you can't select an item from it. I haven't seen anything else in the forums or anywhere else with other people having this issue so not sure if it's something anyone has come across

## Answer

**Ivan Zhekov** answered on 10 Jun 2021

Can you share more details to how this conflict is happening: what are you using Tailwind for? are you applying tailwind class names to Telerik components if so, which classes to which components? As a rule of thumb, frameworks from different providers rarely work together well to the extent you would want them to and here is why: Neither Tailwind nor Bootstrap have proper components in their frameworks. Yes, Bootstrap has tables and pagination and a few other things, but not anything near as a specialized component vendor has. As such, the styles they provide are not suited for integrating with other third party vendors. Especially in the case of Tailwind, which provides only utility classes ad no notion of components, you should use Tailwind for the layout and parts of the content you need to customize. Treat the components as black boxes -- just leave them as is, but feel free to customize the rest of your page using Tailwind. If you need, for instance, to make a component 100% wide you can do so with inline styles. But if you need it to appear / disappear on various breakpoints, better use a wrapper around it and control those with Tailwind. You can surely customize a theme using tailwind specific syntax, though it may be tricky, if you are unfamiliar with our styles. And just to emphasis on one last thing: it's not like you can't customize, say a button, with Tailwind class names. You probably could. However, we haven't tested it, nor support it as official scenarios. In other words, applying any third party class names to Telerik or Kendo components will yield dubious results... at best. In the rest of the cases, things may utterly break visually or behave strangely. Which brings me back to my first question from above: how are you using Tailwind and UI for Blazor together? Obviously, we are past "dubious results" and straight into "strange behaviour" territory. Regards, Ivan Zhekov
