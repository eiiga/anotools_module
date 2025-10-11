package com.practice.annotation.anotools_spring.controller;

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
public class UserController {

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
}
