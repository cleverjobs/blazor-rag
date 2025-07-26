# Tabstrip - resetting to default tab

## Question

**Lar** asked on 21 Dec 2022

I have a Tabstrip with 3 tabs. I have buttons on the 2nd tab. I select the 2nd tab and click on a button and the active tab goes back to the 1st tab even when the button I clicked on doesn't do anything. How do I prevent the selected tab from resetting to the first (default) tab?

## Answer

**Larry** answered on 21 Dec 2022

needed to add an attribute --> ButtonType="ButtonType.Button", it seems unpredictable behaviors happen when I forget to add this in
