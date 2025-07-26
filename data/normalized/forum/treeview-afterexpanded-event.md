# TreeView AfterExpanded Event

## Question

**Kev** asked on 14 Sep 2022

In my code I'm setting the ExpandedItems and SelectedItems (single item). I have my TreeView in a scrollable div. Once the TreeView has expanded, I want to scroll the selection into view. In javascript I'm getting the DOM element with the aria-selected="true" tag and calling "scrollIntoView". The problem is, that tag doesn't exist until after the TreeView has expanded. There doesn't seem to be any event tied to after the TreeView has expanded. At the OnAfterRenderAsync event, the TreeView hasn't expanded yet. I can invoke the javascript with a button and it works fine - once the TreeView has expanded. But, I don't want the user to have to click a button to view the selection. Is there a better way to do this?

## Answer

**Hristian Stefanov** answered on 19 Sep 2022

Hi Kevin, I carefully reviewed the situation. Indeed, the case is specific. Now let me shed some light on the possibilities I researched below. You are on the right path - " scrollIntoView " is the best approach here. To make it work, here are the two possible options: Using MutationObserver - this javascript tool notifies about DOM changes and checks if the desired node is rendered after the expansion. Using setTimeout - this javascript function gives time to the desired node to get rendered. Keep in mind that with setTimeout, the time needed can depend on different machines. If you go with this approach, make sure to give enough time. I have prepared a sample project attached (see " treeview-scroll-selected-node.zip ") for you that shows both options from above. You can run and test it to see the results. The project uses ".Net 6 " and Telerik version " 3.6 ". Regards, Hristian Stefanov

### Response

**Kevin** commented on 19 Sep 2022

I went with the setTimeout option. It works great, thanks!
