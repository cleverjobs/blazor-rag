# TelerikSplitter elements getting tabindex="-1" attribute while loading

## Question

**Dav** asked on 23 Oct 2023

In a TelerikSplitter when I click a button that causes data to load, every element at that level and lower gets the attribute tabindex="-1" for a split second and then the property is removed. Is there any function of the Splitter or Loader/LoaderContainer that would do this? This causes explicitly set tabindex attributes to be completely removed. Update/Solution: I determined that this was the result of an intermediate Blazor component calling some JavaScript to disable tabbing on load. This issue is unrelated to the Telerik LoaderContainer.
