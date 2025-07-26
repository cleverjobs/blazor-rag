# Why is css order different in published app?

## Question

**che** asked on 13 Aug 2021

Hello, This might be a Blazor issue and not Telerik, but I don't know yet. I have a TelerikCalendar in a Blazor component (.razor page). I added a style tag to the page after the @using directives. One of the styles I added was: .k-calendar .k-state-selected .k-link { background-color: #009966; } This works when the app is hosted by IIS Express in VS 2019 (see image "1" below). However, if it is hosted by Kestrel or published to my machine's IIS, the order of the css gets changed, and my local style gets overruled (see image "2" below). Any ideas? Thanks! 1. IIS Express (my local css "green" gets applied): 2. IIS-hosted (my local css "green" gets overruled by what I guess is the control's default "orange" styling?):

## Answer

**Marin Bratanov** answered on 13 Aug 2021

Hi, The Telerik components cannot influence the rendering engine of the framework and when/how the <style> tag from component markup are added. What I would advise is that you make your selectors heavier so they take precedence regardless of the style loading order (e.g., add a few selectors to them, even something like "html body <the current selector>" could help). This is generally the best practice when overriding third party styles, your own selectors need to be heavier. The other suggestion I can make is to either move such overrides to your own stylesheet instead of keeping them in a component (a while back <script> tags were disabled in components, style tags were also considered for disabling at that point), or use the CSS isolation feature of the framework (note the caveats with nested components here that apply to all components, not just ours). Regards, Marin Bratanov Progress Telerik
