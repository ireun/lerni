<table class='table'>
    <thead>
    <tr>
        <th>#</th>
        <th>Nazwa usługi</th>
        <th>Status</th>
    </tr>
    </thead>
    <tbody>
        %for x in services:
            % if x.count(None)>0 or len(x)==1:
                <tr class='default'>
                    <td>1</td>
                    <td>${x[0]}</td>
                    <td>Nieznany</td>
                </tr>
            % elif x.count(True)+1==len(x):
                <tr class='success'>
                    <td>1</td>
                    <td>${x[0]}</td>
                    <td>OK</td>
                </tr>
            % elif x.count(True)==0:
                <tr class='danger'>
                    <td>1</td>
                    <td>${x[0]}</td>
                    <td>IS DOWN</td>
                </tr>
            %else:
                <tr class='warning'>
                    <td>1</td>
                    <td>${x[0]}</td>
                    <td>${x.count(True)}/${len(x)-1}</td>
                </tr>
            %endif
        %endfor
    </tr>
    </tbody>
</table>