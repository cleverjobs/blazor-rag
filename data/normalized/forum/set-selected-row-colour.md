# Set selected row colour

## Question

**RobRob** asked on 23 Jan 2023

Hi, I'm struggling to find a simple way to set the selected row colour. I'm using the bootstrap theme. I want to change it to the indigo/tertiary colour in the bootstrap theme but I'm getting nowhere. It's still a light blue. Can you assist please. Many thanks, Rob

### Response

**Rob** commented on 23 Jan 2023

Ok I've managed to get a bit further by adding the following to my app.css: .k-grid.k-selected.k-table-td { background-color: #6f42c1!important; color: #ffffff!important;
} This seems to do the trick. Are there any obvious issues with this method? Many thanks, Rob

### Response

**Yanislav** commented on 26 Jan 2023

Hello Rob, I'm glad to hear that you've managed to find a solution. Thank you for sharing it with the community. In general, it is a good practice to avoid using the "!important" statement. With that being said, I can suggest using a bit different CSS selector with higher specificity. <style>.k-table-tbody.k-table-row.k-selected>.k-table-td { background-color: #6f42c1; color: #ffffff;
}
</style> Thus the "!important" statement is no longer needed. Here is an example: [https://blazorrepl.telerik.com/wdEvGAaV43zOzxdB15](https://blazorrepl.telerik.com/wdEvGAaV43zOzxdB15) Аlso note that the CSS above will affect all the Grids in the current page. If you want to affect only a specific Grid you can apply a custom Class and use it in the CSS rule. <TelerikGrid Class="my-grid" I hope this helps.

### Response

**Rob** commented on 26 Jan 2023

Many thanks Yanislav, Yes I wanted to change all grids to behave the same. I used your example; the only thing I had to do was to add .k-grid to the beginning to get the desired effect. Many thanks for you help and advice. Rob .k-grid.k-table-tbody.k-table-row.k-selected>.k-table-td { background-color: #6f42c1; color: #ffffff;
}

### Response

**Yanislav** commented on 30 Jan 2023

Hello Rob, I'm glad to hear my suggestion was helpful and that you've achieved the desired result. As it seems like the issue is resolved now I will close this thread. If further questions arise, you may reopen it anytime by posting a new reply.
