package fnc;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;

import dto.PathInfoDTO;

public class MkdirsFnc {
	public void makedirs(PathInfoDTO pathdto) {
		String result_message = "";
		// PathInfoDTO pathdto = new PathInfoDTO();
		try {
			
			File def = new File(pathdto.getStrDefPath());
			FileReader fr = new FileReader(def);
			BufferedReader br = new BufferedReader(fr);
			
			String read_line = br.readLine();
			
			while(read_line != null) {
				// System.out.println(read_line);
				String out_dir = pathdto.getStrOutPath() + "/" + read_line;
				File make_dirs_path = new File(out_dir);
				make_dirs_path.mkdirs();
				read_line = br.readLine();
			}
			
			br.close();
			
			result_message = "完了！";
			
		}catch(Exception e){
			result_message = "エラー：" + e;
			
		}finally {
			pathdto.setResultMsg(result_message);
		}
	}
}
