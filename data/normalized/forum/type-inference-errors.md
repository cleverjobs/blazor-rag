# Type inference errors

## Question

**Dav** asked on 10 Dec 2020

Here is my code: 01. <TelerikGrid Data="_enrollments" 02. AutoGenerateColumns="false" 03. PageSize="5" 04. ScrollMode="@GridScrollMode.Scrollable" 05. Height="400px" 06. RowHeight="40" 07. SortMode="@SortMode.Multiple" 08. Sortable="true"> 09. <GridColumns> 10. <GridColumn Field="@nameof(EnrollmentDTO.Id)" /> 11. </GridColumns> 12. <DetailTemplate> 13. @{ 14. var category=context as EnrollmentDTO; 15. <TelerikGrid Data="@category.Device" 16. Height="300px" 17. Pageable="true" 18. Sortable="true" 19. PageSize="5" 20. AutoGenerateColumns="true"> 21. </TelerikGrid> 22. } 23. </DetailTemplate> 24. </TelerikGrid> If I remove the DetailTemplate this works fine. Otherwise I get the following errors CS1662 Cannot convert lambda expression to intended delegate type because some of the return types in the block are not implicitly convertible to the delegate return type --and-- CS0411 The type arguments for method 'TypeInference.CreateTelerikGrid_1<TItem>(RenderTreeBuilder, int, int, IEnumerable<TItem>, int, string, int, bool, int, bool, int, int, int, bool)' cannot be inferred from the usage. Try specifying the type arguments explicitly. I cannot figure out what is going on.

## Answer

**David** answered on 10 Dec 2020

Soon after posting this I figured it out. I think it's getting late... @category.Device is not a collection, it's just an object! So I made a collection and added the Device to it: var category=context as EnrollmentDTO; List<EnrollmentDeviceDTO> devices=new List<EnrollmentDeviceDTO>(); <TelerikGrid Data="@devices" Height="300px" Pageable="true" Sortable="true" PageSize="5" AutoGenerateColumns="true"> </TelerikGrid>
