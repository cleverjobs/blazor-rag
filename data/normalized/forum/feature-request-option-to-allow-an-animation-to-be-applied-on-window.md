# [Feature Request] Option to allow an animation to be applied on Window

## Question

**Adr** asked on 20 Mar 2021

I have an AnimationContainer component which I have configured to Slide Left from the right hand side of the viewport. The animation is working just right. I've tried putting a Window component inside the AnimationContainer component hoping that the Window would appear from the right hand side of the viewport as it slowly animates sliding left. What actually happens is the AnimationContainer component continues to animate and slide in left slowly but the Window component just abruptly appears on screen with no animation. When the AnimationContainer component is closed it slides back slowly to the right hand side of the viewport and the Window component remains visible for a few more milliseconds afterwards, before it abruptly disappears. It would be a good feature to add to the product to allow a Window component to use animations whether that be by adding an animation property to the Window component directly or by making the AnimationContainer component work better with the Window component. Thanks.

## Answer

**Marin Bratanov** answered on 21 Mar 2021

Hello Adrian, There are a few separate concepts here, and I will list them in turn: The Window component renders on its own, and is not bound by its parent node, that's a very important feature so it can be positioned and dragged anywhere. Thus, it cannot and should not inherit animations and positioning rules from parent components such as an animation container or drawer. Removing the parent (drawer) from the rendering will dispose the child (the window), however and it will hide together with its parent (but not when its parent is hidden with css - display: none). To animate the window, you need a feature that animates the window itself, its parent is a completely separate structure. You can Follow the implementation of such a feature here: [https://feedback.telerik.com/blazor/1462921-animation-for-window.](https://feedback.telerik.com/blazor/1462921-animation-for-window.) I've added your Vote to it to raise its priority already, and clicking the Follow button will send you emails for updates. In the meantime, you can try animating it with CSS3 animations. Putting a window on the right hand side of the screen - you can see how to do that in the following article: [https://docs.telerik.com/blazor-ui/knowledge-base/window-align-to-right.](https://docs.telerik.com/blazor-ui/knowledge-base/window-align-to-right.) Regards, Marin Bratanov Progress Telerik
