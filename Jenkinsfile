
node("master")
{


stage 'Gated Build'

 checkout scm
sh  '''
           
             echo ' Running the Build steps  '
             
              # Adding Tag    
            git tag -a ${BUILD_TAG} -m 'CI commit tag';
         	
            # Remove the HTTP origin 
            git remote rm origin;
         	
            # Add the SSH origin
            git remote add origin "git@github.com:viveknangal/devops.git";
         			
             # Push the tag 
             git push origin ${BUILD_TAG};
             cat .git/config

            
      '''
      git credentialsId: 'c0a0b94a-b43e-421a-a97a-b8aeaf429a4d', url: 'git@github:viveknangal/devops'
 sh '''  
             cat .git/config
	     git fetch --tags;
             
	     # Print all the Tags
	     git tag;
	  
	     # Merge the Pull Request Tag
	     git merge ${BUILD_TAG};
	  
	     #Push the code
	     git push origin master
         '''
}
