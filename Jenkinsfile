
node("master")
{


stage 'CI Build'

 checkout scm
	
 sh  '''
           echo " This is a CI build Step"
	   ## Here specify the steps for running your CI build steps
	   ## for instance refer below pseudo code for node.js Application
	   ###### Build Steps #######
	   # npm install
	   # npm run webpack
	   ##########################
 
 
     '''
stage 'Merge Build'	
     sh  '''
            echo " This is a Merge Build Step"
            
	    # Adding Tag    
            git tag -a ${BUILD_TAG} -m 'CI commit tag';
         	
            # Remove the HTTP origin 
            git remote rm origin;
         	
            # Add the SSH origin
            git remote add origin "git@github.com:viveknangal/devops.git";
         			
             # Push the tag 
             git push origin ${BUILD_TAG};
            

            
      '''
      git credentialsId: 'c0a0b94a-b43e-421a-a97a-b8aeaf429a4d', url: 'git@github.com:viveknangal/devops'
      
      sh '''  
             
	     git fetch --tags;
             
	     # Merge the Pull Request Tag
	     git merge ${BUILD_TAG};
	  
	     #Push the code
	     git push origin master
       '''
}
