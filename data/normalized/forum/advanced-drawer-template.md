# Advanced Drawer Template

## Question

**Sco** asked on 29 Sep 2020

I was wondering if anyone has tried a more advanced drawer template that works with a collapsible hierarchy menu that is still fully useable in its collapsed form? The menu found in TFS / Azure DevOps is an excellent example of something like this. The selected section shows all the subsections and other sections become flyouts for the subsection. A combo of the Drawer and TreeView or Context Menu might work well for this scenario

## Answer

**Marin Bratanov** answered on 29 Sep 2020

Hi Scott, While someone from the community might chime in later with what they have done, I can suggest you consider the following options: showing the context menu when you want: [https://docs.telerik.com/blazor-ui/components/contextmenu/integration](https://docs.telerik.com/blazor-ui/components/contextmenu/integration) and using it as a navigation tool: [https://docs.telerik.com/blazor-ui/components/contextmenu/navigation](https://docs.telerik.com/blazor-ui/components/contextmenu/navigation) or a tooltip for more options where you can put whatever you need in its template: [https://docs.telerik.com/blazor-ui/components/tooltip/template](https://docs.telerik.com/blazor-ui/components/tooltip/template) Regards, Marin Bratanov

### Response

**Javier** answered on 25 Mar 2021

Good Morning. I am looking for the same, I use TelerikDrawer for Blazor. I have not been able to get the effect, I leave an example video of what I am looking for. I hope you can help me. The 3 suggested links lead to the same site. Greetings.

### Response

**Marin Bratanov** answered on 26 Mar 2021

Hello, You can use, instead of a drawer, a vertical menu with the desired images for the first level: how to make a vertical menu: [https://docs.telerik.com/blazor-ui/components/menu/orientation](https://docs.telerik.com/blazor-ui/components/menu/orientation) how to use images in the menu: [https://docs.telerik.com/blazor-ui/components/menu/icons](https://docs.telerik.com/blazor-ui/components/menu/icons) I've also fixed the links in my previous post, I don't know how it came to be that they are all the same one, I've missed that somehow. If you do create such a layout example - be that with the drawer or menu, I would encourage you to fork this repo and open a pull request with a basic example of the concept (we award such contributions with Telerik points): [https://github.com/telerik/blazor-ui](https://github.com/telerik/blazor-ui) Regards, Marin Bratanov
