# Selecting multiple rows of multiple pages in a grid with a server-side pager system

## Question

**Kév** asked on 09 Mar 2022

Hello, I am currently working on grids with a server side pager system. [https://docs.telerik.com/blazor-ui/components/grid/manual-operations](https://docs.telerik.com/blazor-ui/components/grid/manual-operations) Recently I wanted to add multiple line selection but with the server side pager I can't get a correct behavior. My SelectedItems variable which contains the list of selected items keeps the selected items despite the change of page but on the other hand when I come back to a page with selected items, the checkboxes are not checked. In addition I can reselect them which adds them several times in my list. Do you have an example of a server-side paging system with multiple line selection?

## Answer

**Marin Bratanov** answered on 10 Mar 2022

Hello, Make sure the Equals comparison is correct: [https://docs.telerik.com/blazor-ui/components/grid/selection/overview#selecteditems-equals-comparison](https://docs.telerik.com/blazor-ui/components/grid/selection/overview#selecteditems-equals-comparison) Regards, Marin Bratanov

### Response

**Kévin** commented on 11 Mar 2022

Thank you for your answer, your link helped me a lot. I had to override the "Equals" and "GetHashCode" methods of my object because the server doesn't add items in my list when changing pages but returns me a complete list so the object references are different. My override: # region Override /* Utilisé pour la comparaison de la grid Telerik blazor */ public override bool Equals ( object obj ) { if (obj is null )
{ return false;
} if ( this.GetType() !=obj.GetType())
{ return false;
} // !=V_LabelRefsInfo if (!(obj is V_LabelRefsInfo))
{ return false;
} return ( this.LR_Id==(obj as V_LabelRefsInfo).LR_Id)
&& ( this.ARLR_Id==(obj as V_LabelRefsInfo).ARLR_Id)
&& ( this.AR_Id==(obj as V_LabelRefsInfo).AR_Id);
} public override int GetHashCode ( )=> (LR_Id, ARLR_Id, AR_Id).GetHashCode(); # endregion Thanks again,
