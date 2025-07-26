# Using Windows Authentication on Intranet app, can we get current user name at startup, available then for any CRUD service?

## Question

**Ant** asked on 12 Dec 2021

Currently I have nine service classes in this, my first Blazor app (.Net 6). Each service contains the usual async Tasks required for CRUD, eg GetStudyFees, CreateStudyFee, UpdateStudyFee. So, since this is a data intensive intranet app, which is I believe considered just the thing Blazor Server is good for, in each service I need a connection string ( I'm using Dapper), and I need the current user name, since we want to save CreatedBy and ModifiedBy. This is how I've set this up for one service: private readonly string _conn; private readonly AuthenticationStateProvider _auth; public StudyFeeService ( IConfiguration config, AuthenticationStateProvider auth ) {
_conn=config.GetConnectionString( "PharmCTConn" );
_auth=auth;
} public async Task<string> GetUser ( ) { var authState=await _auth.GetAuthenticationStateAsync(); var user=authState.User; return user.Identity.Name;
} public async Task<bool> CreateStudyFee ( StudyFeeViewModel studyFee ) { var parameters=new DynamicParameters();
studyFee.CreatedBy=await GetUser();

parameters.AddDynamicParams( new {
studyFee.HREC,
studyFee.Fee,
studyFee.CreatedBy
}); using ( var conn=new SqlConnection(_conn))
{ string query=@"insert into dbo.StudyFee (HREC, Fee, CreatedBy)
values (@HREC, @Fee, @CreatedBy)"; await conn.ExecuteAsync(query, parameters, commandType: CommandType.Text);
} return true;
} I could duplicate this code at the top of each of my service classes, but instead is there a way that the GetUser Task could be run in Program.cs perhaps, making the username then available by injection for all services to access? I have read quite a bit around this, including StackOverflow, but being inexperienced both with Blazor and .Net Core, I haven't been able to work it out. The app will only open once the user has logged in using Windows Authentication - there is no anonymous user.

### Response

**Antony** commented on 12 Dec 2021

Actually, yes, I'm repeating that GetUser() method in each service, but it's simple and short - and often the alternative is not so simple and short - so I'm happy. But if you do know a neat and elegant alternative, it might be useful to a lot of people.

### Response

**Deasun** commented on 31 Aug 2023

Might be reading wrong, but cant you build a global class to keep the userid in. Just fill that in with your userId from getuser() in the index page. Then on the others read from the Globalstuff.userid ?
