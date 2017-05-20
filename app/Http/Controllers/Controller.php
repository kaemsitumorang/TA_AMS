<?php

namespace App\Http\Controllers;

use Illuminate\Foundation\Bus\DispatchesJobs;
use Illuminate\Routing\Controller as BaseController;
use Illuminate\Foundation\Validation\ValidatesRequests;
use Illuminate\Foundation\Auth\Access\AuthorizesRequests;
use Illuminate\Support\Facades\Input;

class Controller extends BaseController
{
    use AuthorizesRequests, DispatchesJobs, ValidatesRequests;

    public function RetrievedTweet(){
    	$slang_word = Input::get('slang_word');
    	exec("/usr/local/bin/python /Users/Kaemsitumorang/PDB/public/w2v.py '{$slang_word}'", $output, $return);
		if ($return) {
		    throw new \Exception("Error executing command - error code: $return");
		    dd($return);
		}
		$status = '';
		$a=[];
		$i=0;
		foreach ($output as $value) {
			if ($i==0) {
				$status = $value;
			}
			else{
				array_push($a,$value);	
			}
			$i=$i+1;
		    	
		}

		
		// exec("/Users/Kaemsitumorang/anaconda/bin/python /Users/Kaemsitumorang/PDB/public/project_pdb.py '{$username}'", $output, $return);
		// $output = shell_exec('RET=`docker cp /Users/Kaemsitumorang/PDB/public/tweet.txt 4e39bb4b4fea:/`;echo $RET');
		// echo $output;
		// $output2 = shell_exec('RET=`docker exec 4e39bb4b4fea hdfs dfs -put tweet.txt`;echo $RET');
		// echo $output2;
		// $output3 = shell_exec('RET=`docker exec 4e39bb4b4fea spark-submit twitter_app.py`;echo $RET');
		// echo $output3;
    	return redirect('/')->with('hasil', $a)->with('query', $slang_word)->with('stat', $status);

    }
}
