package gui;

import java.awt.FlowLayout;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JOptionPane;
import javax.swing.JTextField;

import dto.PathInfoDTO;
import fnc.MkdirsFnc;

public class InputGui extends JFrame implements ActionListener{
	/*
	 * フィールド宣言
	 * ・定義ファイルパス（フルパス）
	 * ・出力ファイルパス（フルパス）
	 * ・「作成」ボタン
	 */
	JTextField txt_input_def_path = new JTextField(30);
	JTextField txt_output_dir_path = new JTextField(30);
	JButton btn_make_dirs = new JButton("作成");
	
	// コンストラクタ
	public InputGui(){
		// GUI画面の設定
		getContentPane().setLayout(new FlowLayout());
		
		// テキストボックス設置
		getContentPane().add(txt_input_def_path);
		getContentPane().add(txt_output_dir_path);
		
		// 送信ボタンの設置
		getContentPane().add(btn_make_dirs);
		
		// 送信ボタンの処理設定
		btn_make_dirs.addActionListener(this);

		// GUIを閉じた時、プログラムも終了
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		
		// サイズを設定
		setSize(400, 150);
		
		// GUI画面の可視化
		setVisible(true);
	}
	
	public void actionPerformed(ActionEvent ae) {
		// ボタン押下時の処理
		if(ae.getSource() == btn_make_dirs) {
			// DTOクラスのインスタンス
			PathInfoDTO pathdto = new PathInfoDTO();
			
			// 定義ファイルパスをセット
			pathdto.setStrDefPath(txt_input_def_path.getText());
			
			// 出力先のディレクトリパスをセット
			pathdto.setStrOutPath(txt_output_dir_path.getText());
			
			MkdirsFnc mf = new MkdirsFnc();
			mf.makedirs(pathdto);
			
			JOptionPane.showMessageDialog(null,
					pathdto.getResultMsg(),
					"ディレクトリ作成処理",
					JOptionPane.INFORMATION_MESSAGE);
			
		}
	}
}
