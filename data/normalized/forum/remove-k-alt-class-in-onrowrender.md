# Remove k-alt Class in OnRowRender

## Question

**Sud** asked on 22 Dec 2021

I have a grid where the last few rows show different types of totals with different color highlighting. In the OnRowRenderHandler, I assign the background-color via CSS like args.Class="bc_orange". This works fine unless the row also has the k-alt class in which case it overrides the background color. Is there a way in the OnRowRender to remove the k-alt class? Normally in JQuery I would use the .removeClass function. public void OnRowRenderHandler ( GridRowRenderEventArgs args ) {
Models.Results item=args.Item as Models.Results; switch (item.row)
{ case 1:
args.Class="bc_orange disable-hover"; break; case 2:
args.Class="bc_lightgreen disable-hover"; break; case 3:
args.Class="bc_lightblue disable-hover"; break;
}
}

## Answer

**Dimo** answered on 23 Dec 2021

Hello Eric, OnRowRender can add custom classes, but does not remove built-in ones. In this case, please use higher specificity for your CSS rule. The alt row style has specificity 0, 2, 1: .k-grid tr.k-alt { background-color: rgba ( 0, 0, 0,. 04 );
} For example, specificity 0, 2, 2 (or higher) will surely work: div.k-grid tr.bc_orange { background-color: orange;
} In theory, other options include: edit the theme CSS file and remove the k-alt rule build the theme from our source, after removing the k-alt rule Both require a bit more effort, but may be worth it, if you need a lot of customizations like this. Regards, Dimo

### Response

**Jakub** commented on 20 Sep 2022

Hi Dimo, what you propose with higher specifity doesn't work in this case. Because if I do that, the browser will still ignore the class I add in OnRowRender so it doesn't solve anything. Why can't we have a Grid property to disable alt class? If you want to dynamically assign color of the grid rows via OnRowRender it's nearly impossible to do it in convenient way Jakub

### Response

**Joana** commented on 22 Sep 2022

Hello Jakub, I am adding my response from the support ticket in the forum, so that it can be transparent to everyone. The purpose of the `OnRowRender` event is to provide customization on top of the built-in theme of the Grid. We might be able to provide a setting in the EventArgs that would define whether to persist the existing row styling.However, we need to validate it and observe the demand. I understand that this is an urgent matter for you. So, let me go through the possible solutions that you have also mentioned. 1. Use javascript to remove the k-alt class It is possible to have a MutationObserver in the application that tracks for the presense of such class, and removes it. This approach brings complexity to the app and I personally consider the css solution a better one. 2. Use css An alternative is to override the default k-alt class styles in the app. Then, you can use the OnRowRender event to provide both alternate rows style and custom highlighted rows. I have created a REPL snippet that uses stronger css selector to assure the correct styling is applied, but the same can be achieved throuh an `!important` rule: [https://blazorrepl.telerik.com/mQOXwlml1329apuc16](https://blazorrepl.telerik.com/mQOXwlml1329apuc16) You might customize the themes through our ThemeBuilder that will persist your theme configuration and assure easy update of the styles: [https://themebuilder.telerik.com/blazor-ui](https://themebuilder.telerik.com/blazor-ui)
