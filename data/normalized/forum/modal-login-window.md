# Modal Login Window?

## Question

**Jon** asked on 20 Apr 2020

Hi Any ideas how I can create a Modal Login Window on startup? and validate a user / pass? I have done this before using the Telerik ASP.Net - RadWindow. thx in advance

## Answer

**Marin Bratanov** answered on 21 Apr 2020

Hi Jonathan, The Window component is just a container. You can put any content in it (including a form with textboxes). The key thing is implementing the login feature in your Blazor app - once you have it running in a simple <div> that you show with a simple @if-block, you can do the same with the Window (but it's easier to show by binding its Visible parameter to the field, without the if-block). The articles from MSDN here and here can help you get started. If you create such a sample, feel free to open a pull request and post it in this repo, we award such contributions with Telerik points: [https://github.com/telerik/blazor-ui.](https://github.com/telerik/blazor-ui.) Regards, Marin Bratanov
