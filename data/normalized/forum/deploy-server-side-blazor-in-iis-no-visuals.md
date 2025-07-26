# Deploy Server Side Blazor in IIS , no visuals

## Question

**Ger** asked on 07 May 2019

Dear Telerik, I have deployed our server-side Blazor app to our IIS Server. Everything works except , the Telerik Controls have no Visuals (CSS) ? De Grid has no gridlines, the command buttons haven no icon, the tab-headers are rendered vertically, all fonts are black . I have attached a screenshot. Is there something I have missed or should do ? regards, Gert

## Answer

**Marin Bratanov** answered on 07 May 2019

Hello Gert, It looks like our theme stylesheet is not being loaded. Could you check the browser dev toolbar to see what happens with the network request for it? You can reference it from the cloud as shown in Step 3 in the following section: [https://docs.telerik.com/blazor-ui/getting-started/server-blazor#add-to-existing-project.](https://docs.telerik.com/blazor-ui/getting-started/server-blazor#add-to-existing-project.) Note how the @symbol is escaped for razor: <link id="kendoCss" rel="stylesheet" href=" [https://unpkg.com/](https://unpkg.com/) @@progress/kendo-theme-default @@latest/dist/all.css" /> You can also open the resulting link in a browser, save the contents, and use them as a local asset for the time being if you cannot access the cloud, or you don't want to use a package manager like libman. Regards, Marin Bratanov

### Response

**Gert** answered on 07 May 2019

Hello Marin, my fault, turned out that our Server blocked de external CSS-file. I used libman which is build in .Net core and it works now. Amazing ! thx for the fast response, Gert

### Response

**Marin Bratanov** answered on 07 May 2019

I'm glad you have things working, Gert. On a side note, you may find interesting the npm + SASS approach I used in the following sample app, as it can be useful if you customize Bootstrap, and you want to use our Bootstrap Theme too (or if you also want to bundle and minify styles): [https://github.com/telerik/blazor-dashboard.](https://github.com/telerik/blazor-dashboard.) I'm not saying it is better than libman (certainly is a bit more complex), it's just a different way to manage dependencies that may be useful. --Marin
