# Bootstrap vs Telerik vs Kendo

## Question

**Rud** asked on 15 Jan 2022

I'm a relative Newbie to web programming and Blazor. I'm wondering if I still need Bootstrap if now I have Telerik. Does Telerik replace the need to use bootstrap? Or do I have to use both (e.g. for making the layout with bootstrap but use telerik controls)? If not, can I remove the bootstrap scripts? And what is this Kendo thing (which is over and over across the Telerik website)? Is it another way to theme my app? Do I have to busy myself with this? TIA

## Answer

**Marin Bratanov** answered on 17 Jan 2022

Hello Rudi, These are three separate and distinct things. Bootstrap is tooling for creating layouts as its base (CSS), and nowadays there are many JS plugins for it. This is not related to any of the Telerik or Kendo components (even though we have some integration on styling our components to match Bootstrap styles, see more here ). This section also offers some potential alternatives to bootstrap. For some of the JS widgets in bootstrap - it is up to you to decide whether to use them, they are not something we handle in any way. I think that we have native Blazor components for most, if not all of the built-in ones they have, though, so you may want to browser our demos to see what we offer. So, whether you keep or remove bootstrap scripts is up to you, just keep in mind that it is very unlikely that the Blazor framework has any integration with them and so using them to touch the DOM may lead to unpleasant surprises after a re-render. As for Kendo - this is a line of UI components very similar to the UI for Blazor product, they just have a different brand name and step on different technologies (like jQuery, React, Angular, Vue). The common ground they have with the Blazor components is that they share the themes (CSS styling) and HTML rendering. I hope this explains the situation. Regards, Marin Bratanov

### Response

**Rudi** commented on 17 Jan 2022

Hi Marin, yep, that helped. Thanks a lot! Best Regards Rudi
