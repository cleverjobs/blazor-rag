# Expand Grid-Height to a GridLayout Row-Height

## Question

**Hen** asked on 11 May 2023

I would like to achieve this: I have a GridLayout width 3 Rows (50px, Auto, 50px) The second row is expanding due to the Browser-Height. Inside this second Row I would like to put a Grid that expands along to the maximum available height when the User resizes the Browser. If I give the Grid the Height of "100%" the Height is too low if the Grid has no rows. I would like to expand the Grid always to the maximum available space. At the moment I try to calculate the height with JavaScript in Pixel but I hope that there would be a better way !? Is there any ?

## Answer

**Nadezhda Tacheva** answered on 15 May 2023

Hi Hendrik, To achieve the desired behavior, I would recommend keeping the Grid height at 100% but calculating the height of the second GridLayout row depending on the viewport instead of setting it to auto. You can use the CSS calc() - subtract the height of the other rows and any other elements or paddings from the total viewport height. I've prepared a basic example to showcase the approach: [https://blazorrepl.telerik.com/QRafvpPH32GCrUXp38.](https://blazorrepl.telerik.com/QRafvpPH32GCrUXp38.) In this case, I take the 100% viewport height (100vh) and I subtract 100px (the total of the other two rows) and two times 24px which are the top and bottom paddings. I hope you will find that useful. Please let us know if any other questions appear. Regards, Nadezhda Tacheva Progress Telerik

### Response

**Hendrik** commented on 16 May 2023

Hello Nadezhda, thank you very much for your time and effort. Your sample works but honestly are my use cases a little bit more complicated. Because I am allowing the user to choose between different themes (small, medium, large) I can not use fixed heights in my rows and a viewport height of 100vh is also never used, because on top of the Grid/Gridlayout are sometimes other components like menubar, etc. So I could calculate the height of the relevant row and I do it already but I was hoping to get a more generic approach because my own calculations do not fit 100%. I am struggeling a little bit with css and I was hoping to get just a Class/Property that is doing the trick....

### Response

**Nadezhda Tacheva** commented on 18 May 2023

Hi Hendrik, I am sorry that you are having a hard time working with CSS. Generally speaking, it is possible to set a custom Class to the GridLyout to alter it as needed. However, you will still be dealing with styling and layout modifications that should be controlled by the application and not by the component itself. If the layout will be dynamically changed based on the user preferences, you may work with relative units for the GridLayout and its inner elements and not fixed ones. It is also possible to dynamically change the size of the GridLayout itself and this can also be done in a relative manner. For example: [https://blazorrepl.telerik.com/cRupvWPE23IXtAHg25.](https://blazorrepl.telerik.com/cRupvWPE23IXtAHg25.) If you are facing difficulties with the specific setup, I can put you in touch with our Professional Services team. They specialize in tailor-made solutions and custom coding. Please let me know if you are interested in that option and I can start the process for you.
