# Remove Margin from FormItems in First Row

## Question

**Lel** asked on 02 Apr 2024

When using the TelerikForm's Columns parameter, the FormItems in the first row will have a margin just like FormItems in later rows. I want to remove the extra margin on the top. This can be seen in the example on the Form Columns page. After starting the Preview, use developer tools (F12) and select either of the FormItems in the first row. You will see a margin of 14 (dark brown colored area). Then if you go to Edit, remove the Columns="2", and restart the Preview, you will see the first FormItem does not have a margin, while the remaining FormItems have the margin, which is the desired behavior.

## Answer

**Leland** answered on 02 Apr 2024

The workaround I'm currently using is to add a custom css class to the TelerikForm element with: margin-top: - 14px Things look correct when displayed, but when you use developer tools you can see that the form is really overlapping with the component above it, which would make it difficult to troubleshoot other styling issues involving those components, and it could have some other side effects.

### Response

**Tsvetomir** answered on 05 Apr 2024

Hi Leland, Thank you for sharing your scenario in such detail. Indeed, when you use the " margin-top: -14px " CSS class, the form component overlaps the upper one. Therefore, to avoid this, you can apply the following CSS to the form items only in the first row: <style>.k-form-layout> div:nth-child (-n+ @Columns ) { margin-top: 0;
} </style> <TelerikForm Model="@FormModel" Columns=" @Columns " ColumnSpacing="25px" Width="700px"> </TelerikForm> @code {
private Person FormModel { get; set; }=new Person(); private int Columns { get; set; }=2; public class Person
{
public int Id { get; set; }
public string FirstName { get; set; }
public string LastName { get; set; }
public DateTime DOB { get; set; }=DateTime.Today.AddYears(-20);
public string CompanyName { get; set; }
public DateTime HireDate { get; set; }
public bool IsOnVacation { get; set; }=true;
}
} Regards, Tsvetomir Progress Telerik
