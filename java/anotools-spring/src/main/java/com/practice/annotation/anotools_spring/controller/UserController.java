package com.practice.annotation.anotools_spring.controller;

import com.practice.annotation.anotools_spring.dto.UserDTO;
import com.practice.annotation.anotools_spring.service.UserInfoService;
import com.practice.annotation.anotools_spring.service.UserService;
import java.util.List;
import java.util.Map;
import java.util.Optional;
import lombok.RequiredArgsConstructor;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.autoconfigure.security.SecurityProperties.User;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
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

  @Autowired
  private final UserInfoService userInfoService;

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
    return userService.getUserRandomId();
  }

  @GetMapping("/users/info/all")
  public List<UserDTO> getAllUser() {
    return userInfoService.selectAllUser();
  }

  @GetMapping("/users/info/{id}")
  public ResponseEntity<?> getOneUser(@PathVariable Long id) {
    Optional<UserDTO> userOpt = userInfoService.selectOneUser(id);

    if (userOpt.isPresent()) {
      return ResponseEntity.ok(userOpt.get());
    } else {
      return ResponseEntity.status(HttpStatus.NOT_FOUND)
          .body(Map.of("message", "User not found"));
    }
  }
}
