# Razor - TelerikFileManager - How to manage displayed fields when I have FileManagerViewType.Grid?

## Question

**Ada** asked on 21 Mar 2025

Hello At the moments I have default view FileManagerViewType.Grid and I see grid with fields - File name ,Date , File size. What to do to display only Filename I am not interested in changing from Grid to ListView There should be a FileManagerViewType.Grid with just the file name. How to manage displayed fields when I have FileManagerViewType.Grid? Best Regards

## Answer

**Anislav** answered on 21 Mar 2025

Your scenario is not directly supported by the component. However, you can apply a workaround by hiding the unnecessary columns using CSS, like this: <style> th [data-col-index]:not ( [data-col-index="0" ] ), td [data-col-index]:not ( [data-col-index="0" ] ) { display: none!important;
} </style> You may need to refine the selectors to ensure that only the intended table is affected. Additionally, this approach leaves empty spaces where the hidden columns were. To improve the layout, consider adjusting the width of the "Name" column with some CSS to utilize the available space. Regards, Anislav Atanasov

### Response

**Adam** answered on 21 Mar 2025

Thanks Anislav I solved this problem according to your suggestions via css, but it's not very elegant. Do you(Telerik company) plan to parameterize these attributes, e.g. to display more or less information about the file?

### Response

**Anislav** commented on 21 Mar 2025

Hi Adam, I’m not part of Telerik, so I can’t answer your question directly, but I doubt they will make such a change. However, you can request this feature here: [https://feedback.telerik.com/blazor.](https://feedback.telerik.com/blazor.) Regards, Anislav Atanasov

### Response

**Hristian Stefanov** commented on 24 Mar 2025

Hi all, As part of the Telerik team, I can confirm that a feature request for customizing the FileManager Grid columns has already been submitted on our public
