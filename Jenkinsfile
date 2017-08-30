
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

            
      '''
      
}
