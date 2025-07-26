# Custom sort function in grid column.

## Question

**Bla** asked on 28 Dec 2021

Hi. I'm wondering if there's a easy way to set a custom order function to a grid column. For example, suppose that I need to sort a column with IP Addresses: 192.168.168.1 192.168.168.2 192.168.168.101 192.168.168.4 192.168.168.20 Usually the grid sort this column like a string, so the result is: 192.168.168.1 192.168.168.101 192.168.168.2 192.168.168.20 192.168.168.4 when the desirable result will be: 192.168.168.1 192.168.168.2 192.168.168.4 192.168.168.20 192.168.168.101 I did several attempts without success. Order by a calculated field created in the column template looks like a workaround more than a real solution. Really don't like it. Reading about the GridState I've found there is a property: SortCompare (part of SortDescriptor) but I can't make it work assigning a function like this: public class IPAddressComparer: IComparer <IpAddress>
{ public int Compare ( IpAddress a, IpAddress b ) { return Enumerable.Zip(
a.Address.Split( '.' ),
b.Address.Split( '.' ),
(x, y)=> int.Parse(x).CompareTo( int.Parse(y)))
.FirstOrDefault(i=> i !=0 );
}
} It seems to be a applicable only for jQuery-based widgets such as UI for ASP.NET MVC. What else can I try? Maybe I'm missing something... can't be so complicated. Blazorist.

## Answer

**Marin Bratanov** answered on 30 Dec 2021

Hi, The way to implement data source operations in a customized fashion is to use the OnRead event and do the work with your business logic there. You can read more about this here: [https://docs.telerik.com/blazor-ui/components/grid/manual-operations.](https://docs.telerik.com/blazor-ui/components/grid/manual-operations.) At the moment, the SortCompare field you can see in the DataSourceRequest is, indeed, a compatibility feature with other suites and is not applicable in the Blazor components. Regards, Marin Bratanov
