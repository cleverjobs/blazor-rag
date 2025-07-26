# 2 different listviews on one page with different k-listview-content styles

## Question

**And** asked on 04 Mar 2022

I have 2 listviews on a single page. On one the items are displayed in a single column... one per row. On the second the items are displayed as a grid. Per the ListView template demo this is done by overriding the k-listview-content class: . k - listview - content { display: grid; grid - template - columns: repeat ( auto - fill, 180px ); gap: 30px 20px; } On that page that screws up the other listview. Is there a different way to achieve this? Andy

## Answer

**Marin Bratanov** answered on 06 Mar 2022

Hi Andy, You can use the Class parameter of the component to set a specific CSS class on each of the listviews so that you can cascade the CSS rules through it and only target the desired instance. Regards, Marin Bratanov Progress Telerik
