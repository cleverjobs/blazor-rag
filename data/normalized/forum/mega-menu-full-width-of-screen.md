# Mega menu full-width of screen

## Question

**Mic** asked on 07 Feb 2023

We are using this example ([https://docs.telerik.com/blazor-ui/knowledge-base/menu-megamenu)](https://docs.telerik.com/blazor-ui/knowledge-base/menu-megamenu)) to make a mega menu in our page header, but we would like to make the popup animation the full-width of the screen. We used this CSS to override the class of the popup, but this also overrides all the other animation popups. We only want to have this full-width for the mega menu animations and not any of the other popups like the dropdownlist or the context menu, etc..k-animation-container { left: 0 !important; width: 100% !important; } We found a similar issue reported in the Kendo UI forums, but suggestion was to use jQuery to detect clicks: [https://www.telerik.com/forums/k-animation-container-1384e3db9853](https://www.telerik.com/forums/k-animation-container-1384e3db9853) Is this there no way to do this with CSS? Seems like it would be beneficial to have some type of unique identifier for the different popups to be able to style them individually.
