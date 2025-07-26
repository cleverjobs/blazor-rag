# Cannot Resize or Reorder columns in a grid

## Question

**Fla** asked on 16 Jan 2020

Hello, I've been trying to implement column reordering and resizing but no luck. Just looking at your demo website for blazor and it does't work either. [https://demos.telerik.com/blazor-ui/grid/column-reordering](https://demos.telerik.com/blazor-ui/grid/column-reordering) [https://demos.telerik.com/blazor-ui/grid/column-resizing](https://demos.telerik.com/blazor-ui/grid/column-resizing)

## Answer

**Marin Bratanov** answered on 16 Jan 2020

Hello Flavien, Thank you for reaching out. We are aware of this problem and it will be corrected in the 2.6.1 release that we will ship today or, at the latest, tomorrow. Would you like me to send you a message here when it is live? Regards, Marin Bratanov

### Response

**Flavien** answered on 16 Jan 2020

Thanks Marin, I'll wait for the release and re-try, no need to notify me.

### Response

**Marin Bratanov** answered on 16 Jan 2020

Hi Flavien, 2.6.1 is live. I wanted to post this here for anyone else, as this is a public thread. Regards, Marin Bratanov

### Response

**wu** answered on 15 Feb 2020

The column resize function is ready,but the resize cusor At the column tail,Instead of between two columns, At the same time,when resizing,the cusor often lost!

### Response

**Marin Bratanov** answered on 15 Feb 2020

Hello Wu, Judging by your other thread, your latency to our demos is very large, which can break a Blazor app. I suggest you try running them locally to test how things work for you. On my end (both locally and on our demos) column resizing works fine (note that in our demos the ID column is not resizable, and that is a deliberate choice to showcase you can disable the feature per column). If you can still reproduce a problem, please open a ticket and send me that reproducible so I can examine it. Regards, Marin Bratanov
