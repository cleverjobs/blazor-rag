# How to remove the word "Sum" at footer of Grid when export data into Excel

## Question

**Chi** asked on 31 May 2023

Hi all, I want to remove the word "Sum", and only keep the number at the footer of the Excel file when I export data from the grid as pictures below. Is there anyone know? Please help me. Thank you

## Answer

**Dimo** answered on 02 Jun 2023

Hi Chinh, Use the OnAfterExport event of the Grid to obtain the exported Excel file. Then use RadSpreadProcessing to modify the desired cell value(s). The example below is based on this one - Custom cell formatting of the exported file with RadSpreadProcessing. Follow the step-by-step instructions there. @using Telerik.Windows.Documents.Spreadsheet.FormatProviders.OpenXml.Xlsx
@using Telerik.Windows.Documents.Spreadsheet.Model

<TelerikGrid Data="@GridData"> <GridExport> <GridExcelExport OnAfterExport="@OnGridAfterExport" /> </GridExport> <GridAggregates> <GridAggregate Field="@nameof(Product.Name)" Aggregate="@GridAggregateType.Count" /> <GridAggregate Field="@nameof(Product.Stock)" Aggregate="@GridAggregateType.Sum" /> </GridAggregates> <GridToolBarTemplate> <GridCommandButton Command="ExcelExport"> Export to Excel </GridCommandButton> </GridToolBarTemplate> <GridColumns> <GridColumn Field="@nameof(Product.Name)"> <FooterTemplate> @context.Count </FooterTemplate> </GridColumn> <GridColumn Field="@nameof(Product.Stock)"> <FooterTemplate> @context.Sum </FooterTemplate> </GridColumn> </GridColumns> </TelerikGrid>

@code {
List<Product> GridData { get; set; }=new List<Product>(); async Task OnGridAfterExport ( GridAfterExcelExportEventArgs args ) { //args.Stream is finalized. XlsxFormatProvider Import() requires a readable stream, //so copy the stream bytes to a new MemoryStream instance which will be used for the import. var bytes=args.Stream.ToArray(); var excelStream=new MemoryStream(bytes); //create a format provider instance to call the import XlsxFormatProvider formatProvider=new XlsxFormatProvider(); //import the stream to a workbook Workbook workbook=formatProvider.Import(excelStream); //get Stock sum cell and remove "Sum: " CellSelection sumCell=workbook.Worksheets[ 0 ].Cells[ new CellIndex(GridData.Count + 1, 1 )];
sumCell.SetValue(sumCell.GetValue().Value.RawValue.Replace( "Sum: ", "" )); //save the modified workbook in a MemoryStream MemoryStream modifiedExportStream=new MemoryStream();
formatProvider.Export(workbook, modifiedExportStream); //pass the modified stream to the event arguments args.Stream=modifiedExportStream;
}

protected override void OnInitialized ( ) {
GridData=new List<Product>(); var rnd=new Random(); for (int i=1; i <=3; i++)
{
GridData.Add( new Product ( ) {
Id=i,
Name=$ "Product {i}",
Stock=rnd.Next( 0, 10 )
});
}
}

public class Product {
public int Id { get; set; }
public string Name { get; set; }=string.Empty;
public int Stock { get; set; }
}
} Regards, Dimo
