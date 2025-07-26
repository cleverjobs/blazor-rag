# Blazor Editor Component Localization

## Question

**Ann** asked on 26 Feb 2021

I want to use Editor component, but I need change language and I have no idea how to do it Found this, but it also doesn't help me [https://demos.telerik.com/blazor-ui/editor/localization](https://demos.telerik.com/blazor-ui/editor/localization) I'm using Blazor WebAssembly

## Answer

**Marin Bratanov** answered on 26 Feb 2021

Hi Anna, I recommend you first review this article to see how localization works for our components: [https://docs.telerik.com/blazor-ui/globalization/localization.](https://docs.telerik.com/blazor-ui/globalization/localization.) Then, go to the "demos" folder of your local Telerik UI for Blazor installation and there you will see the solution with all our online demos - this will let you inspect the source code. The localization is done through a service implemented in the demo app, and switching the current thread culture (on which the localization depends in this example) is done in the standard Blazor way. You can also find sample .resx files in the Resources folder - Messages.resx contains all the keys for our components. Furthermore, you can take a look at the following sample project for localization of Telerik components in WebAssembly: [https://github.com/telerik/blazor-ui/tree/master/common/localization/ClientLocalizationResx.](https://github.com/telerik/blazor-ui/tree/master/common/localization/ClientLocalizationResx.) While it does not have an Editor component in it, it showcases the concept and just adding an editor + updated localization resource files will let you have a localized editor. Regards, Marin Bratanov
