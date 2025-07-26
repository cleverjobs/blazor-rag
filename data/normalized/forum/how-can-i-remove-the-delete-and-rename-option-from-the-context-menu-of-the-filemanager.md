# How can I remove the Delete and Rename Option from the Context Menu of the FileManager

## Question

**Luk** asked on 16 Dec 2022

Blazor File Manager: Selecting and right-clicking Files and Directories in the File Manager gives you the 3 Options "Rename", "Download" and "Delete". I want to disable/not show the Options "Rename" and "Delete". I have customized my Toolbar with custom css. Is there a similar solution to "customize" the context menu (remove "Delete" and "Rename")? Or is there a different solution? Any help would be appreciated.

### Response

**Yanislav** commented on 20 Dec 2022

Hello Lukas, The functionality is not yet available, however, we will allow customizing the context menu in a future version of the product. I added your vote to the request to increase its popularity - we track the gathered community votes in order to prioritize the enhancements. Additionally, you may subscribe to the item to get status updates - this is the easiest way to follow the progress of the feature. Regarding the custom approach to hide some elements in the Context Menu - the case is different than customizing the Toolbar elements. In general, the Context Menu is rendered in a popup with class "k-animation-container". By design, all popup elements in UI for Blazor are rendered on root level and not in their place of declaration. This means that the Context Menu is not technically inside the FileManager and it will not be possible to specifically target it. Theoretically, you can use ' display:none ' CSS rule over the list items in the pop-up, that hold the Delete and Rename options using the "k-animation-container" class as a selector. However, note that this approach is not reliable and I would not recommend it - this class is vastly used amongst the popup elements in UI for Blazor, so this rule will affect any other possible components with dropdowns that you may have on the page. <style>.k-animation-container ul> li:nth-child ( 1 ){ display:none;
}
</style> My recommendation would be to use the built-in option for customizing the Context Menu once available.
