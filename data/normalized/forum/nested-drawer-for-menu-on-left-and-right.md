# Nested drawer for menu on left and right

## Question

**Cla** asked on 04 Sep 2020

Hi, my goal is obtain a layout with a left menu (Push) and a right menu (Overlay) and in the middle the page content. I tried nesting 2 TelerikDrawer objects without success: <TelerikDrawer Data="LeftItems" Mode="DrawerMode.Push" MiniMode="true"> <Content> <TelerikDrawer Data="RightItems" Mode="DrawerMode.Overlay" Position="DrawerPosition.Right"> <Content> ... </Content> </TelerikDrawer> </Content> </TelerikDrawer> The right drawer is not visualized.. How to obtain the desired layout? Thanks

## Answer

**Marin Bratanov** answered on 04 Sep 2020

Hello Claudio, I am attaching below a small sample that shows how this can be done - comments in the code (~/Shared/MainLayout.razor) explain the situation in more details. Regards, Marin Bratanov

### Response

**Claudio** answered on 07 Sep 2020

Thanks Marin, the sample code you attached work well! Only one question related to overlay mode: if the drawer is configured with Push the height of the panel is contained inside parent element, but with Overlay mode the panel fit the full browser height. There is a way to fit the height of the parent element as done with Push mode? Thanks

### Response

**Marin Bratanov** answered on 07 Sep 2020

Hello Claudio, The 100% height is by design (documented here ). Nevertheless, you can review the component rendering and CSS rules in the browser devtools ( this blog post can help you do that) and add rules to get the desired changes. For examle, like this: <style>.limited-height.k-drawer { height: 50%;
} </style> <TelerikDrawer Data="RightItems" Mode="DrawerMode.Overlay" Position="DrawerPosition.Right" @ref="@RightDrawerRef" Class="limited-height"> Regards, Marin Bratanov

### Response

**Marin Bratanov** answered on 09 Sep 2020

I've also added a sample project and explanations in our samples repo: [https://github.com/telerik/blazor-ui/tree/master/drawer/two-drawers](https://github.com/telerik/blazor-ui/tree/master/drawer/two-drawers) Regards, Marin Bratanov

### Response

**Claudio** answered on 09 Sep 2020

Thanks Marin
