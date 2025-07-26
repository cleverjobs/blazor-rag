# Using TravelTemplate, having CSS problems and Intellisense

## Question

**Gle** asked on 09 Dec 2024

The CSS in the travel template works perfectly fine, however in VS2022, I am not getting any intellisense from the CSS at all. When I do class="" and whether I hit the space bar to load intellisense for suggestions, or do CTRL+SPACE I don't get anything. I am usually getting "dismiss" but that is about it. Nothing from reset.css in the wwwroot/common folder or the styles.css from wwwroot/landing/travel are showing either. I am noticing that the CSS in the App.razor file are being received from the unpkg.com link instead of everything being downloaded right to the project and referenced directly. How do I get this all to work? Can I download these files and reference them directly or can I only use unpkg? Does this even work with unpkg?

## Answer

**Dimo** answered on 11 Dec 2024

Hi Glenn, Visual Studio seems to offer CSS intellisense only for local files. I don't see a setting for this, so you can download the two remote stylesheets in App.razor from unpkg.com and register them as local files in wwwroot. Note that duplicate " @" that you need to remove when requesting the files directly in the browser address bar. Regards, Dimo Progress Telerik
