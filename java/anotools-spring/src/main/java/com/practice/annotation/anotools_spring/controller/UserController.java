package com.practice.annotation.anotools_spring.controller;

import com.practice.annotation.anotools_spring.dto.UserDTO;
import com.practice.annotation.anotools_spring.service.UserService;
import java.util.List;
import lombok.RequiredArgsConstructor;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.autoconfigure.security.SecurityProperties.User;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

// Webリクエストを受け取るクラス
@RestController
// メソッドの戻り値を「HTMLビュー」ではなく「JSON」などのレスポンスボディとして返す
@RequestMapping("/api")
@RequiredArgsConstructor
public class UserController {

  @Autowired
  private final UserService userService;

  @PostMapping("/users")
  public User createUser(@RequestBody User user) {
    // 受け取ったUserを加工して返す例
    user.setName(user.getName().toUpperCase());
    return user; // 自動的にJSONで返却される
  }

  @GetMapping("/users/{id}")
  public User getUser(@PathVariable Long id) {
    User user = new User();
    user.setName("test" + id);
    return user;
  }

  @GetMapping("/users/getid")
  public int getUserId() {
    return userService.getUserId();
  }

  @GetMapping("/users/all")
  public List<UserDTO> getAllUser() {
    return userService.selectAllUser();
  }
}
