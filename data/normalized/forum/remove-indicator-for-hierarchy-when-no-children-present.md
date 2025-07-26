# Remove indicator for Hierarchy when no children present

## Question

**Ted** asked on 03 Mar 2020

Is there a way to remove the indicator when no children are returned for a row?

## Answer

**Marin Bratanov** answered on 04 Mar 2020

Hello Ted, You can Follow the implementation of such a feature in this page (I added your Vote for you): [https://feedback.telerik.com/blazor/1430980-conditionally-hide-hierarchical-grid-expand-button](https://feedback.telerik.com/blazor/1430980-conditionally-hide-hierarchical-grid-expand-button) In the meantime, you can add an if-block in the detail template and show a "no data" type of message when there is no data for the child components. Regards, Marin Bratanov
