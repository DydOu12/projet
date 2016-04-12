%if name == 'World':
    <h1>Hello {{name}}!</h1>
    <p>This is a test.</p>
%else:
    <h1>Hello {{name.title()}}!</h1>
    <p>How are you?</p>
%end


<label for="entrainement"> Niveau d'activité choisis </label>
        <select id="entrainement" name="entrainement"> 

%for type in nivact:
        	<option>{{ type }}</option>
        %end

        </select> <br/> <br/>