# TreeView performance

## Question

**Ste** asked on 12 Apr 2022

Hello, I am developing a mission critical application using Blazor and your beautiful components. Alas, I'm in big trouble, because everything is painfully slow. I have been able to solve many problems following the suggestions I found in your documentation, but now I'm stuck, trying to use the TreeView component. I need to show a fully expanded tree with 200/300 nodes, and it takes forever to rendere. Like 5 seconds in debug, and around 4 seconds in release mode. Even trying an AOT release, didn't solve the problem, nor gets it better in any perceptible way. Thi sounds madness to me. I'm starting to heavily regret ot have not chosen React to develop my application... Watching the log window of Chrome during the rendering of the expanded nodes I see thounds of rows like these: "Rendering component NNNN of type Telerik.Blazor.Components.Common.Animation.AnimationGroup" "Rendering component NNNN of type Telerik.Blazor.Components.TreeView.TreeViewNode" "Rendering component NNNN of type Telerik.Blazor.Components.TelerikAnimationContainer" Is it possible in someway to get a more... I dont' know... streamlined rendering of the tree? Even if I do not expand automatically the tree and I leeve the user do it... if, as i can happen, I have the 200/300 nodes all under only one root node, it takes the same time, which, from a user standpoint is simply, and understandably, incomprehensible. Thank you.

## Answer

**Svetoslav Dimitrov** answered on 14 Apr 2022

Hello Stefano, First of all, thank you for the kind words on our components and I am sorry that the performance of the TreeView is not satisfactory. Indeed, when you render a large number of nodes the performance would take a drastic hit. In general, when you render 300 nodes under one root would mean 300 * 4=1200 (the root node is not included) would slow the browser down. We have an open feature request regarding the Virtual scrolling of nodes in the TreeView which would improve the performance. I have added your Vote for it and you can click the Follow button to receive email notifications on status updates. I am sorry to report, that currently, I cannot offer a workaround as even the Load On Demand feature would not render 300 nodes quicker. Regards, Svetoslav Dimitrov Progress Telerik

### Response

**Stefano** commented on 15 Apr 2022

Thank you for the reply. This feature would be much appreciated. In the meantime I need to adapt some javascript tree component to solve my problem. Regards.

### Response

**Svetoslav Dimitrov** commented on 20 Apr 2022

Hello Stefano, I am happy to read that you have a workaround in mind until the Virtual scrolling feature is implemented and released! Thank you for using Telerik UI for Blazor!

### Response

**Stefano** commented on 01 May 2022

Hi Svetoslav. I'm sure it is not your intention, but your answer sounds a little ironic. My "workaround" is to not use the component I paid for and recreate it by myself. Let me tell you that I'm not happy with this solution. Having to wait 5 seconds to see rendered a treeview with 300 nodes on my screen, I was too much incredulous to say anything right away, but after thinking about it long enough I have to conclude that something is really broken, at least with Blazor, and maybe with your blazor component too. Best regards.

### Response

**Svetoslav Dimitrov** commented on 04 May 2022

Hello Stefano, Take my apologies for my misplaced comment and for the inconvenience the lack of the Virtual Scrolling feature. I can understand that the workaround you have implemented is not ideal, and I am sorry to report that I am not able to provide another solution. Rendering a lot of HTML in one go, in Blazor, is an expensive (performance-wise) task and I can see the value of providing the Virtual Scrolling feature. That being said, again, take my apologies that my previous reply sounded ironic, that was not my intention.
