# Static Group within the datasource

## Question

**Mic** asked on 02 Oct 2019

Will the Grid have an update to group within the code like what we can do in Asp.Net Core? I have also noticed that we cannot hide columns, just not rendered. I have hidden columns here to change the Grouping headers. Example: (The grouping starts with line 19, which works in Asp.NET core) 01. @(Html.Kendo().Grid<Scenario>(Model.Scenarios) 02..Name("scenarios") 03..Columns(col=> 04. { 05. col.Bound(c=> c.Task.CodeYear).ClientGroupHeaderTemplate("Survey: #=data.value#").Hidden(true); 06. col.Bound(c=> c.Task.Site.Alias).ClientGroupHeaderTemplate("Site: #=data.value#").Hidden(true); 07. col.Bound(c=> c.ReferenceCode).ClientGroupHeaderTemplate("Scenario No: #=data.value#").Hidden(true); 08. 09. col.Bound(c=> c.Level).ClientTemplate("<a href='" + Url.Content($"/Foundation/Scenarios/Details?id=") + "#=ScenarioId#'><div data-toggle=\"popover\" title=\"#=Level.TypeName# \" data-content=\"#=Level.Description#\">#=Level.ShortName#<span class=\"glyphicon glyphicon-info-sign\"></span></div>").Width(100); 10. 11. col.Bound(c=> c.Risk).Width(150); 12. 13. col.Bound(c=> c.BusinessInterruption).Title("BI").ClientTemplate("#=BusinessInterruption# <a href=\"\\#\" data-toggle=\"popover\" title=\"#=BusinessInterruption#\" data-content=\"#=BIComments#\"><span class=\"glyphicon glyphicon-info-sign\"></span></a>"); 14. col.Bound(c=> c.Workaround).Title("Workaround").ClientTemplate("#=Workaround# <a href=\"\\#\" data-toggle=\"popover\" title=\"#=Workaround#\" data-content=\"#=WorkaroundComments#\"><span class=\"glyphicon glyphicon-info-sign\"></span></a>"); 15. col.Bound(c=> c.MaterialDamage).Title("Material Damage").ClientTemplate("#=MaterialDamage# <a href=\"\\#\" data-toggle=\"popover\" title=\"#=MaterialDamage#\" data-content=\"#=MaterialDamageComments#\"><span class=\"glyphicon glyphicon-info-sign\"></span></a>"); 16. }) 17..DataSource(ds=> 18. ds.Ajax() 19..Group(group=> 20. { 21. group.Add(g=> g.Task.CodeYear); 22. group.Add(g=> g.Task.Site.Alias); 23. group.Add(g=> g.ReferenceCode); 24. }) 25. ) 26..Scrollable() 27. )

## Answer

**Marin Bratanov** answered on 04 Oct 2019

Hi Michael, To each distinct question I see: set grouping in code - at this point, only the user can perform grouping by dragging the column header to the group panel. We intend to expose programmatic control over more feature (like sorting as well), we simply haven't gotten to it. I created the following page where you can Follow its status: [https://feedback.telerik.com/blazor/1432800-set-grouping-from-code.](https://feedback.telerik.com/blazor/1432800-set-grouping-from-code.) hiding columns - in blazor this is done through conditional markup, you can see a similar example here: [https://demos.telerik.com/blazor-ui/grid/columns.](https://demos.telerik.com/blazor-ui/grid/columns.) If setting programmatic grouping works per fields regardless of whether a column is visible for the field, would this suffice for you? Also, perhaps a future version will also have a column list in the column menu where the user may be able to toggle visibility of columns, like in the current Kendo and WebForms grids, but that's a feature that would get implemented further down the road once the suite is more mature and provides the more basic features that must come first. On a side note - I see that the MVC grid you have uses nested models, which is something that is not supported at the moment with Blazor, so you may want to Follow its implementation (I've added your vote): [https://feedback.telerik.com/blazor/1432615-support-for-nested-complex-models.](https://feedback.telerik.com/blazor/1432615-support-for-nested-complex-models.) For the time being you'd have to flatten the model (that is, perhaps to create a view model with the primitive types you need in the view). Regards, Marin Bratanov

### Response

**Michael** answered on 04 Oct 2019

Hello Marin, The grid is only in display mode, so in Blazor, I am using the Template block and displaying the fields I need, which works fine. I was only concerned about programmatically grouping and being able to rename the grouping as I have done above. If we can do the grouping and rename the grouping headers all within the code, I would appreciate that.

### Response

**Marin Bratanov** answered on 04 Oct 2019

Hi Michael, Here's the page you can Follow for group headers customization: [https://feedback.telerik.com/blazor/1432500-group-header-template.](https://feedback.telerik.com/blazor/1432500-group-header-template.) I would still encourage you to review the rest of the information I provided because Blazor has some differences from MVC that I believe you would need to be aware of, migration is not a straight copy-paste path. Regards, Marin Bratanov
