# Add toolbar on bottom of the grid

## Question

**Cla** asked on 15 May 2024

Hi, the grid toolbar is default located on top of the grid, i would like to place it on bottom (without using a separate element). This feature is described in documetation ( [https://docs.telerik.com/blazor-ui/knowledge-base/grid-pager-top-toolbar-bottom](https://docs.telerik.com/blazor-ui/knowledge-base/grid-pager-top-toolbar-bottom) ) as will be implemented in future version of the library. Is this planned? there is a release date? actually i solved with this css, can it be a good workaround? .k-grid.bottom-toolbar {
display: flex;
flex-direction: column-reverse;
} <TelerikGrid Class="bottom-toolbar" /> Thanks

## Answer

**Hristian Stefanov** answered on 15 May 2024

Hi Claudio, I confirm that the workaround you are currently using is OK. Here is the feature request that will make the desired functionality possible with a built-in option: Allow changing the position of the Grid Toolbar. The feature status is still " Unplanned ". That means no specific time frame has been assigned yet. As soon as we move a task to the short-term backlog, the status will change to " Planned ", and most likely a release month will appear as well. In the meantime, if any other alternative solutions appear, I will publicly share them at the above link, as a comment. Additionally, you can receive email notifications with status updates by subscribing to the feature request. Regards, Hristian Stefanov Progress Telerik
