package src.test;

/**
 * @author xiongjl
 * @since 2023/7/28  15:07
 */
public class ExceptionTest {
    public static void main(String[] args) {
        try {
            int i = 10 / 0;
        } catch (Exception e) {
            System.out.println(e.getMessage());
        }
    }
}
