package gui;

import java.awt.FlowLayout;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JOptionPane;
import javax.swing.JTextField;

import dto.PathInfoDTO;
import fnc.MkdirsFnc;

// ディレクトリ作成画面クラス
public class InputGui extends JFrame implements ActionListener{
	/*
	 * フィールド宣言
	 * ・ラベル
	 * 		定義ファイル
	 * 		出力ディレクトリパス
	 * ・テキストボックス
	 * 		定義ファイル（フルパス）
	 * 		出力ディレクトリパス（フルパス）
	 * ・「作成」ボタン
	 */
	JLabel l_input_def_path = new JLabel("定義ファイル（フルパス）：");
	JLabel l_output_dir_path = new JLabel("出力ディレクトリ（フルパス）：");
	JTextField txt_input_def_path = new JTextField(30);
	JTextField txt_output_dir_path = new JTextField(30);
	JButton btn_make_dirs = new JButton("作成");
	
	// コンストラクタ
	public InputGui(){
		// GUI画面の設定
		getContentPane().setLayout(new FlowLayout());
		
		// 定義ファイルパス関連の設置
		getContentPane().add(l_input_def_path);
		getContentPane().add(txt_input_def_path);

		// 出力ディレクトリ関連の設置
		getContentPane().add(l_output_dir_path);
		getContentPane().add(txt_output_dir_path);
		
		// 作成ボタンの設置
		getContentPane().add(btn_make_dirs);
		
		// 作成ボタンの処理設定
		btn_make_dirs.addActionListener(this);

		// GUIを閉じた時、プログラムも終了
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		
		// サイズを設定
		setSize(400, 200);
		
		// GUI画面の可視化
		setVisible(true);
	}
	
	// ボタン押下時の処理
	public void actionPerformed(ActionEvent ae) {
		if(ae.getSource() == btn_make_dirs) {
			// DTOクラスのインスタンス
			PathInfoDTO pathdto = new PathInfoDTO();
			
			// 定義ファイルパスをセット
			pathdto.setStrDefPath(txt_input_def_path.getText());
			
			// 出力先のディレクトリパスをセット
			pathdto.setStrOutPath(txt_output_dir_path.getText());
			
			// ディレクトリ作成処理クラスのインスタンス
			MkdirsFnc mf = new MkdirsFnc();
			
			// ディレクトリ作成処理呼び出し
			mf.makedirs(pathdto);
			
			// ディレクトリ作成処理終了後のメッセージ出力
			JOptionPane.showMessageDialog(null,
					pathdto.getResultMsg(),
					"ディレクトリ作成処理",
					JOptionPane.INFORMATION_MESSAGE);
			
		}
	}
}
