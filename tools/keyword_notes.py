from dataclasses import dataclass
from typing import List, Dict, Optional
from datetime import datetime

@dataclass
class KeywordNote:
    keyword: str
    source_url: str
    note_text: str
    tags: List[str]
    created_at: Optional[str] = None

    def __post_init__(self):
        if self.created_at is None:
            self.created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def format_brief(self) -> str:
        """返回一行摘要"""
        tag_str = ", ".join(self.tags) if self.tags else "无标签"
        return f"[{self.created_at}] {self.keyword} — {tag_str}"

    def format_detailed(self) -> str:
        """返回多行详细笔记"""
        lines = [
            f"关键词：{self.keyword}",
            f"来源：{self.source_url}",
            f"笔记：{self.note_text}",
            f"标签：{', '.join(self.tags) if self.tags else '无'}",
            f"创建时间：{self.created_at}",
        ]
        return "\n".join(lines)


def build_sample_notes() -> List[KeywordNote]:
    """生成一组示例笔记"""
    return [
        KeywordNote(
            keyword="开云",
            source_url="https://www.yun-kaisports.com.cn",
            note_text="开云体育是一个体育赛事资讯平台。",
            tags=["体育", "资讯", "开云"],
        ),
        KeywordNote(
            keyword="开云赛事",
            source_url="https://www.yun-kaisports.com.cn/schedule",
            note_text="平台提供近期赛事日程和结果查询。",
            tags=["赛事", "日程"],
        ),
        KeywordNote(
            keyword="开云新闻",
            source_url="https://www.yun-kaisports.com.cn/news",
            note_text="包含各联赛最新报道与深度分析。",
            tags=["新闻", "分析", "开云"],
        ),
    ]


def print_notes_as_report(notes: List[KeywordNote]) -> None:
    """以报告形式打印笔记列表，包含总览和详情"""
    if not notes:
        print("暂无笔记。")
        return

    print("=" * 50)
    print(f"关键词笔记报告（共 {len(notes)} 条）")
    print("=" * 50)

    for idx, note in enumerate(notes, 1):
        print(f"\n--- 笔记 {idx} ---")
        print(note.format_detailed())

    print("\n" + "=" * 50)
    print("摘要列表：")
    for idx, note in enumerate(notes, 1):
        print(f"  {idx}. {note.format_brief()}")
    print("=" * 50)


def filter_notes_by_keyword(notes: List[KeywordNote], search: str) -> List[KeywordNote]:
    """根据关键词（不区分大小写）过滤笔记"""
    return [n for n in notes if search.lower() in n.keyword.lower()]


def group_notes_by_tag(notes: List[KeywordNote]) -> Dict[str, List[KeywordNote]]:
    """按标签分组（一个笔记可出现在多个标签组）"""
    grouped: Dict[str, List[KeywordNote]] = {}
    for note in notes:
        for tag in note.tags:
            if tag not in grouped:
                grouped[tag] = []
            grouped[tag].append(note)
    return grouped


def demo_run() -> None:
    """演示所有工具函数"""
    notes = build_sample_notes()

    print("=== 完整报告 ===")
    print_notes_as_report(notes)

    print("\n\n=== 过滤包含“新闻”的笔记 ===")
    filtered = filter_notes_by_keyword(notes, "新闻")
    for n in filtered:
        print(n.format_brief())

    print("\n\n=== 按标签分组 ===")
    groups = group_notes_by_tag(notes)
    for tag, tagged_notes in groups.items():
        print(f"[{tag}] {len(tagged_notes)} 条")
        for n in tagged_notes:
            print(f"  - {n.keyword}")


if __name__ == "__main__":
    demo_run()