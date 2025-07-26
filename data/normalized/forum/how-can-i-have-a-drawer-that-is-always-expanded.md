# How can I have a drawer that is always expanded?

## Question

**Dav** asked on 06 Sep 2023

I set Expanded="true" but after I select the second item in the drawer it collapses. Here is my code for the drawer: <TelerikDrawer Data="@pageData" SelectedItem="selectedItem" Mode="@DrawerMode.Push" Expanded="true" MiniMode=true SelectedItemChanged="((DrawerItem item)=> SelectedItemChangedHandler(item))"> <DrawerContent> @{
if (selectedItem is not null)
{ <AdAccount AdAccountDisplayItem="@adAccountDI" /> }
} </DrawerContent> </TelerikDrawer>

## Answer

**Hristian Stefanov** answered on 07 Sep 2023

Hi David, We have a knowledge base article that offers a detailed guide and includes a runnable sample that shows how to prevent the drawer from collapsing on item click. You can access it via this link: Prevent Drawer from collapsing on item click. I encourage you to review the article and apply the approach outlined there. If you encounter any challenges while going through the material or if there are any additional aspects of your scenario that I may have overlooked, please don't hesitate to reach out. Regards, Hristian Stefanov Progress Telerik

### Response

**Víctor** answered on 14 Sep 2023

This workaround is doesen't work for all cases. If I put a dropdown inside the drawer the drawer closes when I select and item in the dropdown. I tied this but it doesen't seem to work: <div @onclick:stopPropagation> @DetailTemplate </div> Can you add a bool property to toggle this behaviour?

### Response

**Hristian Stefanov** commented on 18 Sep 2023

Hi Víctor, I've made an attempt to recreate the issue you've described by integrating a DropDownList within the Drawer component. However, on my end, I observed that the Drawer remains expanded even after selecting values from the DropDownList. It's possible that I may be overlooking a configuration detail that you are testing, which could help me reproduce this behavior. To assist me in better understanding the scenario and providing a tailored solution, would it be possible for you to share the specific configuration you are testing with? You can conveniently utilize REPL instead of sharing an entire project, which will enable me to thoroughly investigate the issue. I look forward to hearing from you. Kind Regards, Hristian
