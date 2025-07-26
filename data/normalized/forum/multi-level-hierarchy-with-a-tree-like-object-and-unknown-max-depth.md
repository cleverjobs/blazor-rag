# Multi-Level Hierarchy with a tree-like object and unknown max depth

## Question

**Joh** asked on 10 Dec 2020

Hello, I've been trying to use a grid with hierarchy to show a list of items, which can have a parent and any number of children. My object looks like this : public class HierarchicObject { public ValueObject value; public List<HierarchicObject> children; } The data that will vary a lot, and the maximum depth cannot be assumed. Everything I have read on the docs and forums leads me to the conclusion that each level of depth has to be declared manually and individually. For example, the code from this page creates 3 levels for different objects.No problem so far. My problem is that I can't do this since there is no known max depth, and even then it would mean duplicating the code many times, making it very large and unreadable as the fields (from my ValueObject) used in the grid contain templates. My object being "hierarchical" by nature, is there a way to make it so the grid can handle virtually any level of depth using a single DetailTemplate or something similar ? Please let me know if you need any additionnal information. Regards

## Answer

**Nadezhda Tacheva** answered on 11 Dec 2020

Hi Johnny, For the described scenario it might be a better approach to try the TreeList component. It is commonly used to display hierarchical data and it also supports the functionalities that the Grid provides (such as sorting, filtering, data editing). You can also check its Load on Demand option that provides the opportunity to improve the performance of your application by requesting less data at any given time. In your case will be also useful since you can use the OnExpand event to check if the current node has children and whether you need to load items for it. Here is also a link to the TreeList Load on Demand Live demo to see it in action. Regards, Nadezhda

### Response

**John** answered on 11 Dec 2020

Hi Nadezhda, Thanks for answering, I learned about TreeList after creating this post and it indeed is more appropriate. I have managed to get it working, though I have a little problem with the display I'd like to share with you, if I may. When a text is longer than the column width, it does a line break but the next line doesn't take into account the depth level and starts at the very left. ( See image 1) I have tried to use the CSS property "white-space", but every value of it gives me a result like Image 2. I wanted to try changing the row height to force a 1-Line display but I couldn't find a row height attribute for the treeList, How can I make sure everything is aligned? Thanks Regards

### Response

**John** answered on 11 Dec 2020

I uploaded the 2 images in the wrong order. "Image 1" and "Image 2" refer to treelist1.png and treelist2.png, respectively.

### Response

**Nadezhda Tacheva** answered on 16 Dec 2020

Hi Johnny, You can still achieve the desired aligning with a little custom CSS but with a different approach. To better illustrate the solution I have created this knowledge base article. You will find screenshots of the expected behavior in both cases (aligned, not aligned) as well as a simple example how to use the Class property of the TreeList to style only its elements, not all instances on the page/app. I hope you will find this information useful. Regards, Nadezhda
