# Visible property removed

## Question

**Rya** asked on 18 Oct 2019

The AnimationContainer's Visible property is no longer available in version 2.2.0 which is a breaking change for us. Is there another way to initialize the AnimationContainer in a visible state without calling the Show() or Toggle() methods?

## Answer

**Marin Bratanov** answered on 18 Oct 2019

Hello Ryan, Indeed, it was removed, and that change was documented here: [https://docs.telerik.com/blazor-ui/upgrade/breaking-changes/2-2-0.](https://docs.telerik.com/blazor-ui/upgrade/breaking-changes/2-2-0.) Calling its methods is the way to show, hide and toggle it now: [https://docs.telerik.com/blazor-ui/components/animationcontainer/overview.](https://docs.telerik.com/blazor-ui/components/animationcontainer/overview.) The component renders in its place of declaration, so if want to use simple visibility binding, you can use a generic if-statement and simple <div> elements. Regards, Marin Bratanov

### Response

**Ryan** answered on 18 Oct 2019

Thanks Marin! I'll make sure to read the upgrade notes next time!

### Response

**Marin Bratanov** answered on 18 Oct 2019

You may also find useful the upgrade instructions and troubleshooting: [https://docs.telerik.com/blazor-ui/upgrade/overview.](https://docs.telerik.com/blazor-ui/upgrade/overview.) Regards, Marin Bratanov
